import React, { Component } from "react";
import BtnBold from "./components/BtnBold";
import BtnNormal from "./components/BtnNormal";
import NavComponent from "./components/NavComponent";
import Footer from "./components/Footer";
import vehiclePhoto from "./assets/img/stock1.png";
import { Link } from "react-router-dom";
import './ViewVehicle.css';
import PdfIcon from "./assets/icons/picture-as-pdf.svg";

const vehicle = {
    id: 1,
    name: "Renault Otaku 2022",
    price: "53789000",
}


const copAmount = Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' }).format(vehicle.price);

class ViewVehicle extends Component {
    render() {
        return (
            <div id="view-vehicle">
                <NavComponent />
                <div className="info-vehicle-container">
                    <div className="info-vehicle__left">
                        <picture>
                            <img src={vehiclePhoto} alt="" />
                        </picture>
                        <div>
                            <h2>Description</h2>
                            <p>
                                Cupidatat irure do quis incididunt duis quis
                                non id dolor aliquip quis deserunt culpa labore.
                                Irure consequat adipisicing voluptate
                                reprehenderit. Esse consectetur excepteur sint
                                eiusmod quis elit magna.
                            </p>
                        </div>
                    </div>
                    <div className="info-vehicle__right">
                        <div className="info-vehicle__right--details">
                            <article>
                                <h2 id="vehicle--name">{vehicle.name}</h2>
                                <p><span>Precio:</span> {copAmount}</p>
                                <p>Compralo hoy y recogelo en 15 días.</p>
                                <p>Hasta <span>108 cuotas</span> ¡Endeudate toda la vida si quieres!</p>
                            </article>
                            <div className="buttons-actions">
                                <Link to={`/pay-single-cart/${vehicle.id}`}>
                                    <BtnBold>Comprar</BtnBold>
                                </Link>
                                <Link to={`/added-cart/${vehicle.id}`}>
                                    <BtnNormal>Agregar al carrito</BtnNormal>
                                </Link>
                            </div>
                        </div>
                        <div>
                            <h2>Ficha tecnica</h2>
                            <picture className="picture-download">
                                <span>Descargar </span>
                                <img src={PdfIcon} alt="" />
                            </picture>
                        </div>
                    </div>
                </div>
                <Footer />
            </div>
        )
    }
}

export default ViewVehicle;