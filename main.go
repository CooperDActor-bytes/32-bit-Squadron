package main

import (
	"bytes"
	"embed"
	"image"
	"image/color"
	_ "image/png"
	"log"

	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/ebitenutil"
)

//go:embed assets/*
var assets embed.FS

var (
	player  *ebiten.Image
	enemies *ebiten.Image
	scaling float64 = 1
)
func init() {
	// Load Player
	playerData, err := assets.ReadFile("assets/player.png")
	if err != nil {
		log.Fatal("failed to load player: ", err)
	}
	imgP, _, _ := image.Decode(bytes.NewReader(playerData))
	player = ebiten.NewImageFromImage(imgP)

	// Load Enemies
	enemyData, err := assets.ReadFile("assets/enemies.png")
	if err != nil {
		log.Fatal("failed to load enemies: ", err)
	}
	imgE, _, _ := image.Decode(bytes.NewReader(enemyData))
	enemies = ebiten.NewImageFromImage(imgE)
}

type Game struct{}

func (g *Game) Update() error {
	return nil
}

func (g *Game) Draw(screen *ebiten.Image) {
	player_op := &ebiten.DrawImageOptions{}
	player_op.GeoM.Translate(100, 100)
	player_op.GeoM.Scale(1*scaling, 1*scaling)
	enemy_op := &ebiten.DrawImageOptions{}
	enemy_op.GeoM.Translate(200, 200)
	enemy_op.GeoM.Scale(1*scaling, 1*scaling)

	// equations for player poition px = x / 2 - 50 * scaling py = y - 100 * scaling
	screen.Fill(color.RGBA{0, 50, 0, 255})
	ebitenutil.DebugPrint(screen, "v1.1.0-Alpha1")
	screen.DrawImage(enemies, enemy_op)
	screen.DrawImage(player, player_op)
}

func (g *Game) Layout(outsideWidth, outsideHeight int) (screenWidth, screenHeight int) {
	return ebiten.WindowSize()
}

func main() {
	ebiten.SetWindowSize(960, 540)
	ebiten.SetWindowTitle("32-bit Squadron")
	ebiten.SetWindowResizingMode(ebiten.WindowResizingModeEnabled)

	iconData, err := assets.ReadFile("assets/32bit Squadron logo.png")
	if err == nil {
		img, _, _ := image.Decode(bytes.NewReader(iconData))
		ebiten.SetWindowIcon([]image.Image{img})
	}
	// ---------------------------

	if err := ebiten.RunGame(&Game{}); err != nil {
		log.Fatal(err)
	}
}