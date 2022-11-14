import React, { Component } from 'react';
import NavComponent from './components/NavComponent';
import ImageSlider from './components/ImageSlider';
import Footer from './components/Footer';
import steering from './assets/icons/steering-2.svg';
import mapPin from './assets/icons/map-pin-2.svg';
import handCoin from './assets/icons/hand-coin.svg';
import BtnLight from './components/BtnLight';
import vehicle1 from './assets/img/stock1.png';
import vehicle2 from './assets/img/stock2.png';
import vehicle3 from './assets/img/stock3.png';
import vehicle4 from './assets/img/stock4.png';
import { Link } from 'react-router-dom';
import "./Home.css";


class Home extends Component {
  render() {

    const slides = [
      { url: "https://i.imgur.com/8lxEjbX.png", title: "Slider 1", },
      { url: "https://i.imgur.com/jP2wkJG.png", title: "Slider 2", },
      { url: "https://i.imgur.com/Vgq0CTu.png", title: "Slider 2", },
    ]

    const containerStyles = {
      width: "100%",
      height: "480px",
      background: "#FFF",
    }

    return (
      <div>
        <NavComponent />
        <div style={containerStyles}>
          <ImageSlider slides={slides} />
        </div>

        <main className="main-container">
          <div className="main__sections">
            <Link to="/vehiculos" className="main__links">
              <div className='section'>
                <img src={steering} alt="" />
                <h3>Nuestro catálogo</h3>
              </div>
            </Link>
            <a href="#About" className="main__links">
              <div className='section'>
                <img src={mapPin} alt="" />
                <h3>¿Dónde estamos?</h3>
              </div>
            </a>
            <Link to="/cotizar" className="main__links">
              <div className='section'>
                <img src={handCoin} alt="" />
                <h3>Cotiza aquí</h3>
              </div>
            </Link>
          </div>
          <h1 className="main__title">¡Encuentra tu próximo vehículo!</h1>

          <div className="main__vehicles">
            <div className="main__vehicle">
              <img src={vehicle1} alt="" />
              <h3>Toyota Corolla</h3>
              <Link to="/cotizar" className="main__links">
                <BtnLight>Ver más</BtnLight>
              </Link>
            </div>
            <div className="main__vehicle">
              <img src={vehicle2} alt="" />
              <h3>Toyota Corolla</h3>
              <Link to="/cotizar" className="main__links">
                <BtnLight>Ver más</BtnLight>
              </Link >
            </div>
            <div className="main__vehicle">
              <img src={vehicle3} alt="" />
              <h3>Toyota Corolla</h3>
              <Link to="/cotizar" className="main__links">
                <BtnLight>Ver más</BtnLight>
              </Link >
            </div>
            <div className="main__vehicle">
              <img src={vehicle4} alt="" />
              <h3>Toyota Corolla</h3>
              <Link to="/cotizar" className="main__links">
                <BtnLight>Ver más</BtnLight>
              </Link >
            </div>
          </div>

          <div className="main__about">
            <div className="main__about--text">
              <h2 id="About">
                ¿Qué es MotorShop?
              </h2>
              <p>
                Exercitation sint ea amet pariatur quis nulla tempor esse qui
                eiusmod consectetur velit sunt aliqua. Pariatur officia ut ad
                dolor ipsum eiusmod. Nulla aliquip magna tempor nisi ullamco
                nostrud veniam sint occaecat ullamco proident cupidatat aliquip
                sit. Adipisicing id anim duis culpa cupidatat cillum qui amet
                proident.
              </p>
            </div>
            <div className="main__about--img">
              <img src={vehicle3} alt="about" />
            </div>
          </div>
        </main>

        <Footer />
      </div>
    );
  }
}

export default Home;
