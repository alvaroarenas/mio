import React from 'react';
import NavBar from './components/NavBar/NavBar';
import style from 'styled-components';

const Main = style.main`
  height: 90px;
  display: flex;
  align-items: center;
  justify-content: center;
 `;

const H1 = style.h1`
  font-family: Raleway;
  font-size: 28px;
  font-style: normal;
  font-weight: normal;


`;
const App: React.FC = () => {
  return (
    <div>
      <NavBar title="Mio" />
      <Main>
        <H1>Select and book</H1>
      </Main>
    </div>
  );
};

export default App;
