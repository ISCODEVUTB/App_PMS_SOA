import React, { Component } from "react";
import { Link } from "react-router-dom";
import shopping_cart from "../assets/icons/shopping-cart.svg";
import "./NavBar.css";

class NavShoppingCart extends Component {
    render() {
        return (
            <li class="navbar__nav-item shopping--cart">
                <Link className="shopping-cart--link" to="/carrito">
                    <img src={shopping_cart} alt="shopping_cart" />
                    <span class="shopping--cart__counter">
                        2
                    </span>
                </Link>
            </li>
        );
    }
}

export default NavShoppingCart;