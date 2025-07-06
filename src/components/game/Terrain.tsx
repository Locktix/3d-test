import { useMemo } from 'react'

interface TerrainProps {
  zone: string
}

const Terrain = ({ zone }: TerrainProps) => {
  // Couleurs et textures selon la zone
  const zoneConfig = useMemo(() => {
    switch (zone) {
      case 'flaris':
        return {
          groundColor: '#90EE90',
          grassColor: '#228B22',
          waterColor: '#87CEEB',
          size: 50
        }
      case 'saintmorning':
        return {
          groundColor: '#F4A460',
          grassColor: '#8FBC8F',
          waterColor: '#4682B4',
          size: 60
        }
      case 'darkon':
        return {
          groundColor: '#696969',
          grassColor: '#2F4F4F',
          waterColor: '#191970',
          size: 70
        }
      default:
        return {
          groundColor: '#90EE90',
          grassColor: '#228B22',
          waterColor: '#87CEEB',
          size: 50
        }
    }
  }, [zone])

  return (
    <group>
      {/* Sol principal */}
      <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -0.5, 0]} receiveShadow>
        <planeGeometry args={[zoneConfig.size, zoneConfig.size]} />
        <meshStandardMaterial color={zoneConfig.groundColor} />
      </mesh>

      {/* Herbe dispersée */}
      {Array.from({ length: 100 }).map((_, i) => (
        <mesh
          key={i}
          position={[
            (Math.random() - 0.5) * zoneConfig.size,
            0,
            (Math.random() - 0.5) * zoneConfig.size
          ]}
          rotation={[0, Math.random() * Math.PI * 2, 0]}
        >
          <cylinderGeometry args={[0.1, 0.1, 0.5]} />
          <meshStandardMaterial color={zoneConfig.grassColor} />
        </mesh>
      ))}

      {/* Arbres */}
      {Array.from({ length: 20 }).map((_, i) => (
        <group
          key={`tree-${i}`}
          position={[
            (Math.random() - 0.5) * zoneConfig.size * 0.8,
            0,
            (Math.random() - 0.5) * zoneConfig.size * 0.8
          ]}
        >
          {/* Tronc */}
          <mesh castShadow>
            <cylinderGeometry args={[0.3, 0.4, 3]} />
            <meshStandardMaterial color="#8B4513" />
          </mesh>
          {/* Feuillage */}
          <mesh position={[0, 2.5, 0]} castShadow>
            <sphereGeometry args={[1.5, 8, 8]} />
            <meshStandardMaterial color="#228B22" />
          </mesh>
        </group>
      ))}

      {/* Rochers */}
      {Array.from({ length: 15 }).map((_, i) => (
        <mesh
          key={`rock-${i}`}
          position={[
            (Math.random() - 0.5) * zoneConfig.size * 0.9,
            0,
            (Math.random() - 0.5) * zoneConfig.size * 0.9
          ]}
          rotation={[
            Math.random() * Math.PI,
            Math.random() * Math.PI,
            Math.random() * Math.PI
          ]}
          castShadow
        >
          <dodecahedronGeometry args={[0.5 + Math.random() * 0.5]} />
          <meshStandardMaterial color="#696969" />
        </mesh>
      ))}

      {/* Eau (si zone appropriée) */}
      {zone === 'flaris' && (
        <mesh rotation={[-Math.PI / 2, 0, 0]} position={[0, -0.3, 0]}>
          <planeGeometry args={[20, 20]} />
          <meshStandardMaterial 
            color={zoneConfig.waterColor} 
            transparent 
            opacity={0.6}
          />
        </mesh>
      )}

      {/* Montagnes (pour certaines zones) */}
      {zone === 'darkon' && (
        <group>
          {Array.from({ length: 5 }).map((_, i) => (
            <mesh
              key={`mountain-${i}`}
              position={[
                (Math.random() - 0.5) * zoneConfig.size,
                0,
                (Math.random() - 0.5) * zoneConfig.size
              ]}
              castShadow
            >
              <coneGeometry args={[3 + Math.random() * 2, 8 + Math.random() * 4]} />
              <meshStandardMaterial color="#708090" />
            </mesh>
          ))}
        </group>
      )}
    </group>
  )
}

export default Terrain 