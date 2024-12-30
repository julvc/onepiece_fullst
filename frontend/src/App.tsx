import React from 'react';
import { Outlet } from 'react-router-dom';

const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-500 text-white p-4">
        <h1 className="text-xl">One Piece API Project</h1>
      </header>
      <main className="p-4">
        <Outlet />
      </main>
    </div>
  );
};

export default App;
