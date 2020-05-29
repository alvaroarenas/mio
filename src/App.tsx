import React from 'react';
import NavBar from './components/NavBar';
import style from 'styled-components';
import CategoryButton from './components/CategoryButton';

import carIcon from './assets/carIcon.svg';
import cameraIcon from './assets/cameraIcon.svg';
import houseIcon from './assets/houseIcon.svg';
import rocketIcon from './assets/rocketIcon.svg';

const Main = style.main`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
 `;

const TitleSection = style.section`
   height: 90px;
   width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
 `;
const H1 = style.h1`
  font-family: Raleway;
  font-size: 28px;
  font-style: normal;
  font-weight: normal;
  width: 100%;
  text-align: center;
`;

const CategoryList = style.section`
  width: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
`;

const App: React.FC = () => {
  return (
    <div>
      <NavBar title="Mio" />
      <Main>
        <TitleSection>
          <H1>Select and book</H1>
        </TitleSection>

        <CategoryList>
          <CategoryButton label={'Cars'} icon={carIcon} />
          <CategoryButton label={'Houses'} icon={houseIcon} />
          <CategoryButton label={'Tools'} icon={cameraIcon} />
          <CategoryButton label={'Rockets'} icon={rocketIcon} />
        </CategoryList>
      </Main>
    </div>
  );
};

export default App;
