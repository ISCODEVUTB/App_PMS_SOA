import React, { Component } from 'react';
import NavComponent from './components/NavComponent';
import Footer from './components/Footer';
import './PaySingleCart.css';


const dataVehicle = {
    title: "Toyota Prado",
    price: 158000000,
    id: 1
}

const { title, price, id } = dataVehicle;

const copAmount = Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' }).format(dataVehicle.price);


class PaySingleCart extends Component {
    render() {
        return (
            <div>
                <NavComponent />
                <div className="single-pay--container">
                    <div className="single-pay__content">
                        <article>
                            <h2>{title}</h2>
                            <p><span>Total a pagar:</span> {copAmount}</p>
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

export default PaySingleCart;
