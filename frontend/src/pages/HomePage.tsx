import React from 'react';

const HomePage = () => {
    return (
        <div className="text-center">
            <h1 className="text-4xl font-bold mb-4">Bienvenido a One Piece Explorer</h1>
            <p className="text-lg text-gray-700 mb-6">
                Explora el mundo de One Piece: Sagas, frutas, episodios y mucho más.
            </p>
            <img
                src="https://wallpapers.com/images/high/one-piece-pictures-jqb9z37rgh7f2atl.webp"
                alt="One Piece"
                className="w-64 mx-auto"
            />
        </div>
    );
};


export default HomePage;