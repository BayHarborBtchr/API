const mysql = require('mysql2/promise');

const connection = mysql.createPool({
    host: 'db',
    user: 'root',
    password: 'root',
    database: 'proyecto'
});

async function crearfactura(factura) {
    const nombreCliente = factura.nombreCliente;
    const email = factura.email;
    const totalCuenta = factura.totalCuenta;

    const result = await connection.query('INSERT INTO facturas (nombreCliente, email, totalCuenta) VALUES (?, ?, ?)', [nombreCliente, email, totalCuenta]);
    return result;
}

async function traerfactura(id_factura) {
    const result = await connection.query('SELECT * FROM facturas WHERE id = ?', [id_factura]);
    return result[0];
}

async function traerfacturas() {
    const result = await connection.query('SELECT * FROM facturas');
    return result[0];
}

module.exports = {
    crearfactura,
    traerfacturas,
    traerfactura
};
