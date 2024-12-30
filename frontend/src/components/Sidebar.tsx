import React from "react";

const Sidebar = () => {
    //#region Sidebar inicial
    // return (


    // <nav className="p-4 space-y-4">
    //     <h1 className="text-2xl font-bold">One Piece App</h1>
    //     <ul className="space-y-2">
    //         <li><Link to="/">Inicio</Link></li>
    //         <li><Link to="/boats">Botes</Link></li>
    //         <li><Link to="/bows">Arcos</Link></li>
    //         <li><Link to="/chapters">Capítulos</Link></li>
    //         <li><Link to="/characters">Personajes</Link></li>
    //         <li><Link to="/crews">Tripulaciones</Link></li>
    //         <li><Link to="/dials">Diales</Link></li>
    //         <li><Link to="/episodes">Episodios</Link></li>
    //         <li><Link to="/films">Filmes</Link></li>
    //         <li><Link to="/fruits">Frutas</Link></li>
    //         <li><Link to="/hakis">Hakis</Link></li>
    //         <li><Link to="/locations">Lugares</Link></li>
    //         <li><Link to="/luffysgear">Luffy Gears</Link></li>
    //         <li><Link to="/luffystechniques">Luffy Técnicas</Link></li>
    //         <li><Link to="/sagas">Sagas</Link></li>
    //         <li><Link to="/swords">Espadas</Link></li>
    //         <li><Link to="/volumes">Volúmenes</Link></li>
    //     </ul>
    // </nav>

    // );
    //#endregion
    return (
        <div className="flex flex-col bg-gray-900 text-white w-64 h-screen p-4">
            <h1 className="text-2xl font-bold mb-6">One Piece Explorer</h1>

            <nav className="flex flex-col gap-4">
                {/* <a href="/boats" className="hover:bg-gray-800 p-2 rounded">Botes</a> */}
                <a href="/bows" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Arcos</a>
            </nav>

            <nav className="flex flex-col gap-4">
                <a href="/boats" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Botes</a>
            </nav>


            <nav className="flex flex-col gap-4">
                <a href="/chapters" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Capitulos</a>
            </nav>

            <nav className="flex flex-col gap-4">
                <a href="/dials" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Diales</a>
            </nav>

            <nav className="flex flex-col gap-4">
                <a href="/episodes" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Episodios</a>
            </nav>

            <nav className="flex flex-col gap-4">
                <a href="/hakis" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Hakis</a>
            </nav>

            <nav className="flex flex-col gap-4">
                <a href="/locations" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Lugares</a>
            </nav>

            <nav className="flex flex-col gap-4">
                <a href="/luffysgear" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Luffys Gears</a>
            </nav>

            <nav className="flex flex-col gap-4">
                <a href="/luffystechniques" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Luffy Tecnicas</a>
            </nav>

            <nav className="flex flex-col gap-4">
                {/* <a href="/boats" className="hover:bg-gray-800 p-2 rounded">Botes</a> */}
                <a href="/sagas" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Sagas</a>
            </nav>

            <nav className="flex flex-col gap-4">
                {/* <a href="/boats" className="hover:bg-gray-800 p-2 rounded">Botes</a> */}
                <a href="/films" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Peliculas</a>
            </nav>

            <nav className="flex flex-col gap-4">
                {/* <a href="/boats" className="hover:bg-gray-800 p-2 rounded">Botes</a> */}
                <a href="/crews" className="text-lg font-medium hover:bg-gray-800 px-4 py-2 rounded transition">Tripulaciones</a>
            </nav>

        </div>

    );
};

export default Sidebar;
