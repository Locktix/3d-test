import { useGameStore } from '../stores/gameStore'

export const useGameControls = () => {
  const { player, toggleUI, movePlayer } = useGameStore()

  const handleKeyDown = (event: KeyboardEvent) => {
    if (!player) return

    const speed = 0.5
    const { position } = player

    switch (event.key.toLowerCase()) {
      case 'w':
      case 'arrowup':
        movePlayer({ ...position, z: position.z - speed })
        break
      case 's':
      case 'arrowdown':
        movePlayer({ ...position, z: position.z + speed })
        break
      case 'a':
      case 'arrowleft':
        movePlayer({ ...position, x: position.x - speed })
        break
      case 'd':
      case 'arrowright':
        movePlayer({ ...position, x: position.x + speed })
        break
      case ' ':
        // Sauter
        movePlayer({ ...position, y: position.y + 1 })
        setTimeout(() => {
          movePlayer({ ...position, y: position.y })
        }, 200)
        break
      case 'i':
        toggleUI('inventory')
        break
      case 'c':
        toggleUI('character')
        break
      case 'k':
        toggleUI('skills')
        break
      case 'enter':
        toggleUI('chat')
        break
      case 'escape':
        // Fermer toutes les fenêtres
        break
    }
  }

  return { handleKeyDown }
}

export const CONTROLS = {
  MOVEMENT: {
    FORWARD: ['w', 'arrowup'],
    BACKWARD: ['s', 'arrowdown'],
    LEFT: ['a', 'arrowleft'],
    RIGHT: ['d', 'arrowright'],
    JUMP: [' ']
  },
  UI: {
    INVENTORY: ['i'],
    CHARACTER: ['c'],
    SKILLS: ['k'],
    CHAT: ['enter'],
    CLOSE: ['escape']
  }
} 