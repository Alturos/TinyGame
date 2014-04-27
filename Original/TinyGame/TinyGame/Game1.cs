using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
namespace TinyGame
{
    public class Game1 : Microsoft.Xna.Framework.Game {
        GraphicsDeviceManager graphics;
        private class Sprite        {
            public Vector2 Pos, Direction;
            public double frame, frametime, attacktime, index, speed = 128, changeDir, kill, frameSpeed = .33, attackSpeed = .75, shoot = 0;
            public void Draw(SpriteBatch batch, Texture2D sheet) {
                batch.Draw(sheet, Pos, new Rectangle((int)(index) * 32, (int)(frame) * 32, 32, 32), Color.White); 
            }
            public void Update(GameTime gt) {
                frametime += gt.ElapsedGameTime.TotalSeconds;
                if (frametime > frameSpeed) { frame++; frametime = 0; if (frame > 1) frame = 0; }
                attacktime -= gt.ElapsedGameTime.TotalSeconds;
                Pos += Direction * (float)speed * (float)gt.ElapsedGameTime.TotalSeconds;
                bool needChange = false;
                if(Pos.X < 0) {Pos.X = 0; needChange = true;}
                if(Pos.X + 32 > 480) {Pos.X = 480 - 32; needChange = true;}
                if (changeDir != 0 && needChange) Direction.X *= -1;
                if (changeDir != 0 && attacktime <= 0) shoot = 1;
                if (Pos.Y + 32 < 0 || Pos.Y > 600) kill = 1;
            }
        }
        KeyboardState ks, oldKs;
        SpriteBatch spriteBatch;
        SpriteFont font;
        Texture2D sprites;
        List<Sprite> Sprites = new List<Sprite>(), Bullets = new List<Sprite>();
        int score = 0;
        System.Random r = new System.Random();
        public Game1()  {
            graphics = new GraphicsDeviceManager(this);
            graphics.PreferredBackBufferHeight = 600;
            graphics.PreferredBackBufferWidth = 480;
        }
        protected override void LoadContent() {
            spriteBatch = new SpriteBatch(GraphicsDevice);
            sprites = Content.Load<Texture2D>("Content/sprites");
            Sprites.Add(new Sprite() { index = 0, Pos = new Vector2(480/2 - 16, 600-32) });
            for (int i = 1; i < r.Next(8, 25); i++) Sprites.Add(new Sprite() { attackSpeed = System.Math.Max(r.Next(3, 20) * r.NextDouble(), 2), attacktime = System.Math.Max(r.Next(1, 10) * r.NextDouble(), 1), speed = r.Next(40, 128), index = r.Next(1, 3), changeDir = 1, Pos = new Vector2(r.Next(0, 480 - 32), r.Next(0, 16) * 32), Direction = new Vector2(r.Next(0, 2) == 1 ? 1 : -1, 0) });
            font = Content.Load<SpriteFont>("Content/Font");
        }
        protected override void Update(GameTime gameTime) {
            if (Sprites[0].kill > 0) { score = 0; Sprites.Clear(); Bullets.Clear(); LoadContent(); return; }
            if (Sprites.Count == 1) for (int i = 1; i < r.Next(8, 25); i++) Sprites.Add(new Sprite() { attackSpeed = System.Math.Max(r.Next(3, 20) * r.NextDouble(), 2), attacktime = System.Math.Max(r.Next(1, 10) * r.NextDouble(), 1), speed = r.Next(40, 128), index = r.Next(1, 3), changeDir = 1, Pos = new Vector2(r.Next(0, 480 - 32), r.Next(0, 16) * 32), Direction = new Vector2(r.Next(0, 2) == 1 ? 1 : -1, 0) });
            oldKs = ks;
            ks = Keyboard.GetState();
            bool left = ks.IsKeyDown(Keys.Left), right = ks.IsKeyDown(Keys.Right), shoot = ks.IsKeyUp(Keys.Space) && oldKs.IsKeyDown(Keys.Space) && Sprites[0].attacktime <= 0;
            Sprites[0].Direction.X = left && right ? 0 : left ? -1 : right ? 1 : 0;
            for (int i = Sprites.Count - 1; i >= 0; i--) { 
                Sprites[i].Update(gameTime);
                if (Sprites[i].shoot > 0) { 
                    Bullets.Add(new Sprite() { index = 4, Direction = new Vector2(0, 1), Pos = new Vector2(Sprites[i].Pos.X, Sprites[i].Pos.Y - 32), speed = 164, frameSpeed = .20 }); 
                    Sprites[i].attacktime = Sprites[i].attackSpeed; 
                    Sprites[i].shoot = 0; }
                if (Sprites[i].kill > 0) Sprites.RemoveAt(i); }
            if (shoot) { 
                Sprites[0].attacktime = Sprites[0].attackSpeed; 
                Sprites[0].frame = 2; 
                Bullets.Add(new Sprite() { index = 3, Direction = new Vector2(0, -1), Pos = new Vector2(Sprites[0].Pos.X, Sprites[0].Pos.Y - 32), speed = 164, frameSpeed = .20 }); }
            for (int i = Bullets.Count - 1; i >= 0; i--) { 
                for (int j = Sprites.Count - 1; j >= 0; j--) {
                    if (Bullets[i].Direction.Y > 0 && j != 0) continue;
                    else if (Bullets[i].Direction.Y < 0 && j == 0) continue;
                    else if (new Rectangle((int)Bullets[i].Pos.X + 4, (int)Bullets[i].Pos.Y + 4, 24, 24).Intersects(new Rectangle((int)Sprites[j].Pos.X, (int)Sprites[j].Pos.Y, 32, 32)))
                    { Bullets[i].kill = 1; Sprites[j].kill = 1; score += Bullets[i].Direction.Y > 0 ? 0 : 5; continue; }
                }
                Bullets[i].Update(gameTime);
                if (Bullets[i].kill > 0)  Bullets.RemoveAt(i);
            }
            base.Update(gameTime);
        }
        protected override void Draw(GameTime gameTime) {
            GraphicsDevice.Clear(Color.DarkGreen);
            spriteBatch.Begin();
            for (int i = 0; i < Sprites.Count; i++) { Sprites[i].Draw(spriteBatch, sprites); }
            for (int i = 0; i < Bullets.Count; i++) { Bullets[i].Draw(spriteBatch, sprites); }
            spriteBatch.DrawString(font, string.Format("Score: {0}", score), new Vector2(10, 580), Color.AliceBlue);
            spriteBatch.End();
            base.Draw(gameTime);
        }
    }
}