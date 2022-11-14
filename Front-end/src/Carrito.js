import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import BtnBold from './components/BtnBold';
import NavComponent from './components/NavComponent';
import vehicle from './assets/img/stock1.png';
import x_circle from './assets/icons/x-circle.svg';
import './Carrito.css';

const listaCarros = [
    {
        title: "Toyota Prado",
        price: 100100,
        count: 1,
    },
    {
        title: "Toyota Kawaii",
        price: 20000000,
        count: 1,
    },
    {
        title: "Toyota Mitsubishi",
        price: 300000,
        count: 1,
    },
    {
        title: "Toyota Otaku",
        price: 400000,
        count: 1,
    },
    {
        title: "Toyota Otaku",
        price: 400000,
        count: 1,
    },
    {
        title: "Toyota Otaku",
        price: 400000,
        count: 1,
    },
    {
        title: "Toyota Otaku",
        price: 400000,
        count: 1,
    },
    {
        title: "Toyota Otaku",
        price: 400000,
        count: 1,
    }
]

class Carrito extends Component {

    constructor(props) {
        super(props);
        this.state = {
            total: 0,
        }
    }

    render() {
        return (
            <div>
                
                <NavComponent />
                <div className='carrito'>
                    <div className='carrito__items'>
                        <h1>Carrito</h1>
                        {
                            listaCarros.map((carro, indexCarro) => {
                                this.state.total += carro.price;
                                return (
                                    <div className='carrito__item' id={`item${indexCarro+1}`}>
                                        <img className="carrito__item__img" src={vehicle} alt='carro' />
                                        <div className='carrito__item__info'>
                                            <p>{carro.title}</p>
                                            <p>Precio: ${carro.price}</p>
                                            <p>Cantidad: {carro.count}</p>
                                        </div>
                                        <img className='carrito__delete' src={x_circle} alt="" />
                                    </div>
                                )
                            })
                        }
                    </div>
                    <div className='carrito__total'>
                        <p>Total: ${this.state.total}</p>
                        <Link to='/pay-shopping-cart'>
                            <BtnBold>Pagar</BtnBold>
                        </Link>
                    </div>
                </div>
            </div>
        )
    }
}

export default Carrito;
