import React from "react";
import { Link } from "react-router-dom";

const Sidebar = () => {
    return (
        <nav className="p-4 space-y-4">
            <h1 className="text-2xl font-bold">One Piece App</h1>
            <ul className="space-y-2">
                <li><Link to="/">Home</Link></li>
                <li><Link to="/boats">Sagas</Link></li>
                <li><Link to="/bows">Sagas</Link></li>
                <li><Link to="/chapters">Sagas</Link></li>
                <li><Link to="/characters">Sagas</Link></li>
                <li><Link to="/crews">Sagas</Link></li>
                <li><Link to="/dials">Sagas</Link></li>
                <li><Link to="/episodes">Sagas</Link></li>
                <li><Link to="/films">Sagas</Link></li>
                <li><Link to="/fruits">Sagas</Link></li>
                <li><Link to="/hakis">Sagas</Link></li>
                <li><Link to="/locations">Sagas</Link></li>
                <li><Link to="/luffysgear">Sagas</Link></li>
                <li><Link to="/luffystechniques">Sagas</Link></li>
                <li><Link to="/sagas">Sagas</Link></li>
                <li><Link to="/swords">Sagas</Link></li>
                <li><Link to="/volumes">Sagas</Link></li>
            </ul>
        </nav>
    );
};

export default Sidebar;
