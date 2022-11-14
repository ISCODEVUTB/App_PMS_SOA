import React, { Component } from 'react';
import NavComponent from './components/NavComponent';
import Footer from './components/Footer';
import './PayShoppingCart.css';


const dataVehicle = [
    {
        title: "Toyota Prado",
        price: 158000000,
        id: 1
    },
    {
        title: "Toyota Kawaii",
        price: 200000000,
        id: 2
    },
    {
        title: "Toyota Mitsubishi",
        price: 300000000,
        id: 3
    },
    {
        title: "Toyota Otaku",
        price: 257000000,
        id: 4
    },
]

let totalPrice = 0;

for (let i = 0; i < dataVehicle.length; i++) {
    totalPrice += dataVehicle[i].price;
}

const copAmount = Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' }).format(totalPrice);


class PayShoppingCart extends Component {
    render() {
        return (
            <div>
                <NavComponent />
                <div className="shopping-cart-pay--container">
                    <div className="shopping-cart-pay__content">
                        <article>
                            <h2>Items a comprar:</h2>
                            {
                                dataVehicle.map((item, index) => {
                                    return (
                                            
                                            <p>{item.title}: {Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' }).format(item.price)}</p>
                                            
                                    )
                                })
                            }
                            <p><span>Total a pagar: </span> {copAmount}</p>
                        </article>
                        <form>
                            <label for="t-number">
                                <p>Numero de tarjeta</p>
                                <input type="number" name="number" id="t-number" placeholder="***** ***** ***** *****" />
                            </label>
                            <label for="t-name">
                                <p>Nombre del propietario</p>
                                <input type="text" name="name" id="t-name" placeholder="John Doe" />
                            </label>
                            <label for="t-expiration">
                                <p>Fecha de expiracion</p>
                                <input type="date" name="expiration" id="t-expiration" />
                            </label>
                            <label for="t-cvv">
                                <p>CVV</p>
                                <input type="number" name="cvv" id="t-cvv" placeholder="***" />
                            </label>
                            <input className="pay-btn" type="submit" value="Pagar" />
                        </form>
                    </div>
                </div>
                <Footer />
            </div>
        )
    }
}

export default PayShoppingCart;
