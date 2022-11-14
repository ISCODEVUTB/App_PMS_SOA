import React, { Component } from "react";
import { Link } from "react-router-dom";
import logo from "./assets/img/motorshop_logo.png";
import "./SingUp.css";

class SingUp extends Component {
    render() {
        return (
            <div className="background">
                <div class="header">
                    <div class="inner-header flex">
                        <div class="singup">
                            <Link to="/">
                                <img src={logo} alt="logo motorshop" />
                            </Link>

                            <form action="" class="flex">
                                <h2>!Crea tu cuenta!</h2>
                                <label for="u-name">
                                    <input type="text" name="name" id="u-name" placeholder="Nombre" />
                                </label>
                                <label for="e-mail">
                                    <input type="text" name="email" id="e-mail" placeholder="Correo eléctronico" />
                                </label>
                                <label for="pass">
                                    <input type="password" name="password" id="pass" placeholder="Contraseña" />
                                </label>
                                <label for="repit-pass">
                                    <input type="password" name="password" id="repit-pass" placeholder="Repita su contraseña" />
                                </label>
                                 
                                <input type="submit" class="singup-btn" value="Registrarse" />
                            </form>
                        </div>
                    </div>

                </div>

                <div class="content flex">
                    <p>Motorshop | Venta de automóviles </p>
                </div>

            </div>
        )
    }
}

export default SingUp;