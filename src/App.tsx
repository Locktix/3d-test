import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { useEffect, useState } from 'react'
import LoginScreen from './components/LoginScreen'
import GameWorld from './components/GameWorld'
import LoadingScreen from './components/LoadingScreen'
import { useGameStore } from './stores/gameStore'

function App() {
  const [isLoading, setIsLoading] = useState(true)
  const { isLoggedIn } = useGameStore()

  useEffect(() => {
    // Simuler le chargement des ressources
    const timer = setTimeout(() => {
      setIsLoading(false)
    }, 2000)

    return () => clearTimeout(timer)
  }, [])

  if (isLoading) {
    return <LoadingScreen />
  }

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route 
            path="/" 
            element={isLoggedIn ? <GameWorld /> : <LoginScreen />} 
          />
          <Route 
            path="/game" 
            element={<GameWorld />} 
          />
        </Routes>
      </div>
    </Router>
  )
}

export default App 