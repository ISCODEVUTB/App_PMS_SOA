import React, { Component } from 'react';
import NavComponent from './components/NavComponent';
import Footer from './components/Footer';
import carrito from './assets/img/stock1.png';
import './Cotizar.css';


const listaCarros = [
    {
        title: "Toyota Prado",
        id: 1,
    },
    {
        title: "Toyota Kawaii",
        id: 2,
    },
    {
        title: "Toyota Mitsubishi",
        id: 3,
    },
    {
        title: "Toyota Otaku",
        id: 4,
    }
]



class Cotizar extends Component {
    render() {
        return (
            <div>
                <NavComponent />
                <form className='form-cotizar' action=''>
                    <div className='form-cotizar__left'>
                        <label for="select-vehicle">
                            <span>Cotizar:</span>
                            <select name="select" id="select-vehicle">
                                {
                                    listaCarros.map((carro) => {
                                        return (
                                            <option value={carro.id}>{carro.title}</option>
                                        )
                                    })
                                }
                            </select>
                        </label>
                        <img src={carrito} alt="Imagen de un carrito azul" />
                        <p>Conoce los precios y versiones haciendo click aquí o ingresa tus datos y un asesor se comunicara contigo.</p>
                    </div>
                    <div className='form-cotizar__right'>
                        <label for="name">
                            <span>Nombre:</span>
                            <input type="text" name="name" id="name" />
                        </label>
                        <label for="last-name">
                            <span>Apellido:</span>
                            <input type="text" name="last-name" id="last-name" />
                        </label>
                        <label for="email">
                            <span>Correo:</span>
                            <input type="email" name="email" id="email" />
                        </label>
                        <label for="terms">
                            <input className='checkbox-input' type="checkbox" name="terms" id="terms" />
                            <span>Aceptas el tratamiento de datos por parte de Motorshop S.A.S</span>
                        </label>
                        <button className='btn-subtmit' type="submit">Enviar</button>
                    </div>
                </form>
                <Footer />
            </div>
        )
    }
}

export default Cotizar;