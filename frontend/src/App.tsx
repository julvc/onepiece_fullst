import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Superiorbar from './components/Superiorbar';
import HomePage from './pages/HomePage';
// import BoatsPage from './pages/BoatsPage';
// import BowsPage from './pages/BowsPage';
// import ChaptersPage from './pages/ChaptersPage';
// import CharactersPage from './pages/CharactersPage';
// import DialsPage from './pages/DialsPage';
// import FilmsPage from './pages/FilmsPage';
// import FruitsPage from './pages/FruitsPage';
// import HakisPage from './pages/HakisPage';
// import LocationsPage from './pages/LocationsPage';
// import LuffysgearPage from './pages/LuffysgearPage';
// import LuffystechniquesPage from './pages/LuffystechniquesPage';
import SagasPage from './pages/SagasPage';
// import SwordsPage from './pages/SwordsPage';
// import VolumensPage from './pages/VolumesPage';

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex h-screen">
        {/* Sidebar para pantallas grandes */}
        <div className="hidden md:block w-64 bg-gray-900">
          <Sidebar />
        </div>

        {/* Contenido principal */}
        <div className="flex-1">
          {/* Barra superior para pantallas pequeñas */}
          <div className="block md:hidden">
            <Superiorbar />
          </div>

          {/* Contenido dinámico */}
          <div className="p-4">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/sagas" element={<SagasPage />} />
              {/* Agrega más rutas según sea necesario */}
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
};



export default App;
