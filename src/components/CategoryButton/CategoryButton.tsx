import React from 'react';
import styled from 'styled-components';
import { Link } from '@reach/router';

const Button = styled.button`
  background: #ff6b00;
  color: white;
  width: 160px;
  height: 160px;

  font-family: Raleway;
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  line-height: 28px;

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  padding: 0px;

  a {
    text-decoration: none;
    color: white;
  }
`;
const Icon = styled.div`
  margin: 0px;
`;

type CategoryButtonProps = {
  label: string;
  icon?: string;
};

const CategoryButton: React.FC<CategoryButtonProps> = ({ label, icon }) => {
  const image = icon ? (
    <Icon>
      <img src={icon} alt={label} />
    </Icon>
  ) : null;

  return (
    <Button>
      <Link to={`products/${label}`}>
        {image}
        {label}
      </Link>
    </Button>
  );
};

export default CategoryButton;
