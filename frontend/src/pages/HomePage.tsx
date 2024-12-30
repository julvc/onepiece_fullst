import React from 'react';

const mockData = [
    { id: 1, name: 'Monkey D. Luffy', role: 'Captain', bounty: '1,500,000,000' },
    { id: 2, name: 'Roronoa Zoro', role: 'Swordsman', bounty: '320,000,000' },
    { id: 3, name: 'Nami', role: 'Navigator', bounty: '66,000,000' },
];

const HomePage: React.FC = () => {
    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold mb-6">One Piece Crew</h1>
            <table className="min-w-full bg-white border border-gray-200">
                <thead>
                    <tr>
                        <th className="py-2 px-4 border-b">ID</th>
                        <th className="py-2 px-4 border-b">Name</th>
                        <th className="py-2 px-4 border-b">Role</th>
                        <th className="py-2 px-4 border-b">Bounty</th>
                    </tr>
                </thead>
                <tbody>
                    {mockData.map((member) => (
                        <tr key={member.id}>
                            <td className="py-2 px-4 border-b">{member.id}</td>
                            <td className="py-2 px-4 border-b">{member.name}</td>
                            <td className="py-2 px-4 border-b">{member.role}</td>
                            <td className="py-2 px-4 border-b">{member.bounty}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default HomePage;