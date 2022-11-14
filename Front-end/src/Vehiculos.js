import React, { Component } from "react";
import { Link } from "react-router-dom";
import NavComponent from "./components/NavComponent";
import Footer from "./components/Footer";
import vehicle1 from "./assets/img/stock1.png";
import "./Vehiculos.css";


const vehicles_list = [
    {
        title: "Toyota Prado",
        price: "56,970.000,00",
        id: 1
    },
    {
        title: "Toyota Kawaii",
        price: "96,970.000,00",
        id: 2
    },
    {
        title: "Toyota Mitsubishi",
        price: "87,970.000,00",
        id: 3
    },
    {
        title: "Toyota Otaku",
        price: "156,970.000,00",
        id: 4
    }
]




class Vehiculos extends Component {
    render() {
        return (
            <div>
                <NavComponent />
                <div className="vehicles-container">
                    <h3>Nuestro catalogo.</h3>
                    <div className="vehicles-list">
                        {
                            vehicles_list.map((vehicle) => {
                                return (
                                    <Link to={`/detalle/${vehicle.id}`} >
                                        <div className="vehicle-list__item">
                                            <img src={vehicle1} alt="Imagen del producto." />
                                            <h4>{vehicle.title}</h4>
                                            <p>$ {vehicle.price} COP</p>
                                        </div>
                                    </Link>
                                )
                            })
                        }
                    </div>
                </div>
                <Footer />
            </div>
        )
    }
}

export default Vehiculos;