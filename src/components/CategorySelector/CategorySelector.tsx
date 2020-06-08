import React from 'react';
import style from 'styled-components';
import CategoryButton from '../CategoryButton';

import carIcon from '../../assets/carIcon.svg';
import cameraIcon from '../../assets/cameraIcon.svg';
import houseIcon from '../../assets/houseIcon.svg';
import rocketIcon from '../../assets/rocketIcon.svg';

import { RouteComponentProps } from '@reach/router';

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

const CategorySelector: React.FC<RouteComponentProps> = (
  props: RouteComponentProps
) => {
  return (
    <Main>
      <TitleSection>
        <H1>Select and book</H1>
      </TitleSection>

      <CategoryList>
        <CategoryButton category={'Car'} label={'Cars'} icon={carIcon} />
        <CategoryButton category={'House'} label={'Houses'} icon={houseIcon} />
        <CategoryButton category={'Tool'} label={'Tools'} icon={cameraIcon} />
        <CategoryButton
          category={'rocket'}
          label={'Rockets'}
          icon={rocketIcon}
        />
      </CategoryList>
    </Main>
  );
};

export default CategorySelector;
