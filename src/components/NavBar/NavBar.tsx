import React from 'react';
import styled from 'styled-components';

const Header = styled.header`
  background: #0000bf;
  position: relative;
  height: 75px;

  display: flex;
  align-items: center;
  justify-content: center;
`;

const H1 = styled.h1`
  display: block;
  margin: 0 0 0 0;
  font-family: Paytone One;
  font-style: normal;
  font-weight: normal;
  font-size: 36px;
  line-height: 68px;

  color: white;
`;

type NavBarProps = {
  title: string;
};

const NavBar: React.FC<NavBarProps> = ({ title }) => {
  return (
    <Header>
      <H1>{title}</H1>
    </Header>
  );
};

export default NavBar;
