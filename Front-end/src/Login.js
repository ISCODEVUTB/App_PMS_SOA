import React, { Component } from "react";
import { Link } from "react-router-dom";
import logo from "./assets/img/motorshop_logo.png";
import "./Login.css";

class Login extends Component {
    render() {
        return (
            <div className="background">
                <div class="header">
                    <div class="inner-header flex">
                        <div class="login">
                            <Link to="/">
                                <img src={logo} alt="logo motorshop" />
                            </Link>

                            <form action="" class="flex">
                                <h2>¡Accede a tu cuenta!</h2>
                                <label for="e-mail">
                                    <input type="text" name="email" id="e-mail" placeholder="Correo eléctronico" />
                                </label>
                                <label for="pass">
                                    <input type="password" name="password" id="pass" placeholder="Contraseña" />
                                </label>
                                <Link to="/singup">Registrarse.</Link>
                                 
                                <input type="submit" class="login-btn" value="Iniciar sesión" />
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

export default Login;