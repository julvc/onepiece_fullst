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



// const App: React.FC = () => {
//   return (
//     <div className="min-h-screen bg-gray-100">
//       <header className="bg-blue-500 text-white p-4">
//         <h1 className="text-xl">One Piece API Project</h1>
//       </header>
//       <main className="p-4">
//         <Outlet />
//       </main>
//     </div>
//   );
// };

const App = () => {
  return (
    <Router>
      <div className="flex h-screen">
        {/* Sidebar para pantallas grandes */}
        <div className="hidden md:block w-1/5 bg-gray-900 text-white">
          <Sidebar />
        </div>

        {/* Contenido principal */}
        <div className="flex-1">
          {/* Barra superior para pantallas pequeñas */}
          <div className="block md:hidden">
            <Superiorbar />
          </div>

          <div className="p-4">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/sagas" element={<SagasPage />} />
              {/* Agregar rutas para otras páginas */}
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
};


export default App;
