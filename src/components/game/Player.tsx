import { useRef, useEffect } from 'react'
import { useFrame } from '@react-three/fiber'
import { Html } from '@react-three/drei'
import { Player as PlayerType } from '../../stores/gameStore'
import { useGameControls } from '../../utils/controls'
import * as THREE from 'three'

interface PlayerProps {
  player: PlayerType
}

const Player = ({ player }: PlayerProps) => {
  const meshRef = useRef<THREE.Mesh>(null)
  const groupRef = useRef<THREE.Group>(null)
  const { handleKeyDown } = useGameControls()

  // Animation et mouvement
  useFrame((state) => {
    if (meshRef.current && groupRef.current) {
      // Mise à jour de la position
      groupRef.current.position.set(
        player.position.x,
        player.position.y,
        player.position.z
      )
      
      // Rotation du joueur
      groupRef.current.rotation.y = player.rotation.y
      
      // Animation de flottement
      meshRef.current.position.y = Math.sin(state.clock.elapsedTime * 2) * 0.1
    }
  })

  // Gestion des contrôles clavier
  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [handleKeyDown])

  return (
    <group ref={groupRef}>
      {/* Corps du joueur */}
      <mesh ref={meshRef} castShadow receiveShadow>
        <capsuleGeometry args={[0.5, 1, 4, 8]} />
        <meshStandardMaterial 
          color={player.class === 'warrior' ? '#8B4513' : 
                 player.class === 'mage' ? '#4B0082' :
                 player.class === 'archer' ? '#228B22' : '#2F4F4F'}
        />
      </mesh>
      
      {/* Tête */}
      <mesh position={[0, 1.2, 0]} castShadow>
        <sphereGeometry args={[0.3, 16, 16]} />
        <meshStandardMaterial color="#FFE4C4" />
      </mesh>
      
      {/* Épée (si guerrier) */}
      {player.class === 'warrior' && (
        <mesh position={[0.8, 0.5, 0]} rotation={[0, 0, Math.PI / 4]}>
          <boxGeometry args={[0.1, 0.1, 1.5]} />
          <meshStandardMaterial color="#C0C0C0" />
        </mesh>
      )}
      
      {/* Baguette (si mage) */}
      {player.class === 'mage' && (
        <mesh position={[0.6, 0.5, 0]}>
          <cylinderGeometry args={[0.05, 0.05, 1.2]} />
          <meshStandardMaterial color="#8B4513" />
        </mesh>
      )}
      
      {/* Arc (si archer) */}
      {player.class === 'archer' && (
        <mesh position={[0.8, 0.5, 0]} rotation={[0, 0, Math.PI / 2]}>
          <torusGeometry args={[0.4, 0.05, 8, 16]} />
          <meshStandardMaterial color="#8B4513" />
        </mesh>
      )}
      
      {/* Nom du joueur */}
      <Html position={[0, 2.5, 0]} center>
        <div className="bg-black/70 text-white px-2 py-1 rounded text-sm whitespace-nowrap">
          {player.name} Lv.{player.level}
        </div>
      </Html>
      
      {/* Barre de vie */}
      <Html position={[0, 2.2, 0]} center>
        <div className="w-20 h-2 bg-red-900 rounded-full overflow-hidden">
          <div 
            className="health-bar"
            style={{ width: `${(player.health / player.maxHealth) * 100}%` }}
          />
        </div>
      </Html>
    </group>
  )
}

export default Player 