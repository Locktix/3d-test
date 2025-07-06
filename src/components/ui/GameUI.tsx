import { useGameStore } from '../../stores/gameStore'
import { motion, AnimatePresence } from 'framer-motion'
import { 
  Heart, 
  Zap, 
  Star, 
  Package, 
  User, 
  Sword, 
  MessageCircle,
  X
} from 'lucide-react'

const GameUI = () => {
  const { 
    player, 
    showInventory, 
    showCharacter, 
    showSkills, 
    showChat,
    toggleUI 
  } = useGameStore()

  if (!player) return null

  return (
    <div className="game-ui">
      {/* Barres de statut en haut */}
      <div className="absolute top-4 left-4 right-4 flex justify-between items-start">
        {/* Informations du joueur */}
        <div className="bg-black/70 backdrop-blur-sm rounded-lg p-4 text-white">
          <div className="flex items-center gap-2 mb-2">
            <User size={16} />
            <span className="font-medium">{player.name}</span>
            <span className="text-yellow-400">Lv.{player.level}</span>
          </div>
          
          {/* Barre de vie */}
          <div className="flex items-center gap-2 mb-1">
            <Heart size={14} className="text-red-400" />
            <div className="w-32 h-2 bg-red-900 rounded-full overflow-hidden">
              <motion.div 
                className="health-bar"
                initial={{ width: 0 }}
                animate={{ width: `${(player.health / player.maxHealth) * 100}%` }}
                transition={{ duration: 0.3 }}
              />
            </div>
            <span className="text-xs">{player.health}/{player.maxHealth}</span>
          </div>
          
          {/* Barre de mana */}
          <div className="flex items-center gap-2 mb-1">
            <Zap size={14} className="text-blue-400" />
            <div className="w-32 h-2 bg-blue-900 rounded-full overflow-hidden">
              <motion.div 
                className="mana-bar"
                initial={{ width: 0 }}
                animate={{ width: `${(player.mana / player.maxMana) * 100}%` }}
                transition={{ duration: 0.3 }}
              />
            </div>
            <span className="text-xs">{player.mana}/{player.maxMana}</span>
          </div>
          
          {/* Barre d'expérience */}
          <div className="flex items-center gap-2">
            <Star size={14} className="text-green-400" />
            <div className="w-32 h-1 bg-green-900 rounded-full overflow-hidden">
              <motion.div 
                className="exp-bar"
                initial={{ width: 0 }}
                animate={{ width: `${(player.experience / player.maxExperience) * 100}%` }}
                transition={{ duration: 0.3 }}
              />
            </div>
            <span className="text-xs">{player.experience}/{player.maxExperience}</span>
          </div>
        </div>

        {/* Boutons d'action */}
        <div className="flex gap-2">
          <button
            onClick={() => toggleUI('character')}
            className="bg-black/70 hover:bg-black/80 text-white p-3 rounded-lg transition-colors"
          >
            <User size={20} />
          </button>
          <button
            onClick={() => toggleUI('inventory')}
            className="bg-black/70 hover:bg-black/80 text-white p-3 rounded-lg transition-colors"
          >
            <Package size={20} />
          </button>
          <button
            onClick={() => toggleUI('skills')}
            className="bg-black/70 hover:bg-black/80 text-white p-3 rounded-lg transition-colors"
          >
            <Sword size={20} />
          </button>
          <button
            onClick={() => toggleUI('chat')}
            className="bg-black/70 hover:bg-black/80 text-white p-3 rounded-lg transition-colors"
          >
            <MessageCircle size={20} />
          </button>
        </div>
      </div>

      {/* Barre de compétences en bas */}
      <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2">
        <div className="bg-black/70 backdrop-blur-sm rounded-lg p-2 flex gap-2">
          {[1, 2, 3, 4, 5, 6, 7, 8].map((slot) => (
            <div
              key={slot}
              className="w-12 h-12 bg-gray-800 border border-gray-600 rounded-lg flex items-center justify-center text-white text-sm hover:border-gray-400 transition-colors cursor-pointer"
            >
              {slot}
            </div>
          ))}
        </div>
      </div>

      {/* Fenêtres modales */}
      <AnimatePresence>
        {/* Inventaire */}
        {showInventory && (
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.8 }}
            className="absolute inset-4 bg-black/80 backdrop-blur-sm rounded-lg p-6"
          >
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-2xl font-fantasy text-white">Inventaire</h2>
              <button
                onClick={() => toggleUI('inventory')}
                className="text-white hover:text-gray-300"
              >
                <X size={24} />
              </button>
            </div>
            
            <div className="grid grid-cols-8 gap-2">
              {Array.from({ length: 40 }).map((_, i) => (
                <div
                  key={i}
                  className="inventory-slot w-12 h-12 rounded-lg flex items-center justify-center"
                >
                  {player.inventory[i] && (
                    <div className="text-xs text-white text-center">
                      {player.inventory[i].name}
                    </div>
                  )}
                </div>
              ))}
            </div>
          </motion.div>
        )}

        {/* Personnage */}
        {showCharacter && (
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.8 }}
            className="absolute inset-4 bg-black/80 backdrop-blur-sm rounded-lg p-6"
          >
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-2xl font-fantasy text-white">Personnage</h2>
              <button
                onClick={() => toggleUI('character')}
                className="text-white hover:text-gray-300"
              >
                <X size={24} />
              </button>
            </div>
            
            <div className="grid grid-cols-2 gap-6">
              <div className="text-white">
                <h3 className="text-lg font-medium mb-2">Informations</h3>
                <p>Nom: {player.name}</p>
                <p>Classe: {player.class}</p>
                <p>Niveau: {player.level}</p>
                <p>Expérience: {player.experience}/{player.maxExperience}</p>
              </div>
              
              <div className="text-white">
                <h3 className="text-lg font-medium mb-2">Équipement</h3>
                <div className="space-y-2">
                  <div className="flex justify-between">
                    <span>Arme:</span>
                    <span>{player.equipment.weapon?.name || 'Aucune'}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Armure:</span>
                    <span>{player.equipment.armor?.name || 'Aucune'}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Casque:</span>
                    <span>{player.equipment.helmet?.name || 'Aucun'}</span>
                  </div>
                </div>
              </div>
            </div>
          </motion.div>
        )}

        {/* Compétences */}
        {showSkills && (
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.8 }}
            className="absolute inset-4 bg-black/80 backdrop-blur-sm rounded-lg p-6"
          >
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-2xl font-fantasy text-white">Compétences</h2>
              <button
                onClick={() => toggleUI('skills')}
                className="text-white hover:text-gray-300"
              >
                <X size={24} />
              </button>
            </div>
            
            <div className="grid grid-cols-3 gap-4">
              {['Attaque de base', 'Compétence spéciale', 'Sort de guérison', 'Bouclier', 'Charge', 'Explosion'].map((skill, i) => (
                <div
                  key={i}
                  className="skill-button text-center py-4"
                >
                  <div className="text-lg mb-2">⚔️</div>
                  <div className="text-sm">{skill}</div>
                  <div className="text-xs text-gray-400 mt-1">Niveau 1</div>
                </div>
              ))}
            </div>
          </motion.div>
        )}

        {/* Chat */}
        {showChat && (
          <motion.div
            initial={{ opacity: 0, y: 100 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 100 }}
            className="absolute bottom-20 left-4 right-4 bg-black/80 backdrop-blur-sm rounded-lg p-4"
          >
            <div className="flex justify-between items-center mb-2">
              <h3 className="text-white font-medium">Chat</h3>
              <button
                onClick={() => toggleUI('chat')}
                className="text-white hover:text-gray-300"
              >
                <X size={16} />
              </button>
            </div>
            
            <div className="h-32 bg-gray-900 rounded p-2 mb-2 overflow-y-auto text-white text-sm">
              <div className="text-green-400">[Système] Bienvenue dans Flyff Universe Clone!</div>
              <div className="text-blue-400">[Général] Joueur123: Salut tout le monde!</div>
              <div className="text-yellow-400">[Commerce] Vendeur456: Vente d'équipement rare</div>
            </div>
            
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="Tapez votre message..."
                className="flex-1 bg-gray-800 text-white px-3 py-2 rounded border border-gray-600 focus:outline-none focus:border-blue-500"
              />
              <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded">
                Envoyer
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  )
}

export default GameUI 