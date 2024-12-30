import React from "react";

const SagasPage = () => {
    const mockSagas = [
        { id: 1, name: "East Blue Saga", description: "The beginning of Luffy's journey." },
        { id: 2, name: "Alabasta Saga", description: "The battle against Crocodile." },
        // Agregar más datos de prueba...
    ];

    return (
        <div>
            <h1 className="text-3xl font-bold mb-4">Sagas</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {mockSagas.map((saga) => (
                    <div key={saga.id} className="p-4 border rounded shadow">
                        <h2 className="text-xl font-bold">{saga.name}</h2>
                        <p>{saga.description}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default SagasPage;
