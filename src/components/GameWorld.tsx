import { Canvas } from '@react-three/fiber'
import { OrbitControls, Sky, Environment } from '@react-three/drei'
import { Suspense } from 'react'
import { useGameStore } from '../stores/gameStore'
import Player from './game/Player'
import Terrain from './game/Terrain'
import GameUI from './ui/GameUI'
import { EffectComposer, Bloom } from '@react-three/postprocessing'

const GameWorld = () => {
  const { player, currentZone } = useGameStore()

  if (!player) {
    return <div>Erreur: Joueur non trouvé</div>
  }

  return (
    <div className="w-full h-full relative">
      {/* Canvas 3D */}
      <Canvas
        camera={{ position: [0, 5, 10], fov: 75 }}
        shadows
        className="w-full h-full"
      >
        <Suspense fallback={null}>
          {/* Éclairage */}
          <ambientLight intensity={0.4} />
          <directionalLight
            position={[10, 10, 5]}
            intensity={1}
            castShadow
            shadow-mapSize-width={2048}
            shadow-mapSize-height={2048}
          />
          
          {/* Environnement */}
          <Sky sunPosition={[100, 20, 100]} />
          <Environment preset="sunset" />
          
          {/* Terrain */}
          <Terrain zone={currentZone} />
          
          {/* Joueur */}
          <Player player={player} />
          
          {/* Effets visuels */}
          <EffectComposer>
            <Bloom luminanceThreshold={0.5} intensity={0.5} />
          </EffectComposer>
        </Suspense>
        
        {/* Contrôles de caméra */}
        <OrbitControls
          target={[player.position.x, player.position.y, player.position.z]}
          maxPolarAngle={Math.PI / 2}
          minDistance={3}
          maxDistance={20}
        />
      </Canvas>
      
      {/* Interface utilisateur */}
      <GameUI />
    </div>
  )
}

export default GameWorld 