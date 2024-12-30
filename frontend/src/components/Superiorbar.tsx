import React, { useState } from "react";
import { Link } from "react-router-dom";


const Superiorbar = () => {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    return (
        <header className="p-4 bg-gray-900 text-white md:hidden relative">
            <div className="flex justify-between items-center">
                <h1 className="text-xl font-bold">One piece App</h1>
                {/* Botón del menú hamburguesa */}
                <button onClick={toggleMenu} className="text-white focus:outline-none">
                    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                            d="M4 6h16M4 12h16m-7 6h7"></path>
                    </svg>
                </button>
            </div>
            {/* Menú despegable */}
            {menuOpen && (
                <nav className="absolute top-full left-0 w-full bg-gray-800 rounded shadow-lg z-10">
                    <ul className="space-y-2 p-4">
                        <li>
                            <Link to="/" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Inicio</Link>
                        </li>
                        <li>
                            <Link to="/bows" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Arcos</Link>
                        </li>
                        <li>
                            <Link to="/boats" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Barcos</Link>
                        </li>
                        <li>
                            <Link to="/chapters" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Capítulos</Link>
                        </li>
                        <li>
                            <Link to="/dials" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Diales</Link>
                        </li>
                        <li>
                            <Link to="/episodes" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Episodios</Link>
                        </li>
                        <li>
                            <Link to="/hakis" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Hakis</Link>
                        </li>
                        <li>
                            <Link to="/locations" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Lugares</Link>
                        </li>
                        <li>
                            <Link to="/luffysgear" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Luffys Gears</Link>
                        </li>
                        <li>
                            <Link to="/luffystechniques" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Luffy Técnicas</Link>
                        </li>
                        <li>
                            <Link to="/sagas" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Sagas</Link>
                        </li>
                        <li>
                            <Link to="/films" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Películas</Link>
                        </li>
                        <li>
                            <Link to="/crews" 
                            className="block text-lg font-medium text-white hover:bg-gray-700 p-2 rounded"
                            onClick={() => setMenuOpen(false)}>Tripulaciones</Link>
                        </li>
                        
                    </ul>
                </nav>
            
            )}
        </header>
    );
};

export default Superiorbar;