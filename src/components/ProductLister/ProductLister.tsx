import React, { useEffect, useState } from 'react';
import { RouteComponentProps } from '@reach/router';
import styled from 'styled-components';
import loadJsonData from '../../utils/networking';
import arrowIcon from '../../assets/arrowRight.svg';
interface ProductListerProps extends RouteComponentProps {
  category?: string;
}

type Product = {
  name: string;
  description: string;
  image: string;
};

const Article = styled.article`
  margin: 10px;
  padding: 10px;
  border: 0.5px solid rgba(0, 0, 0, 0.15);
  box-sizing: border-box;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  position: relative;
`;

const Image = styled.img`
  width: 100%;
`;

const Header = styled.h3`
  margin-top: 20px;
  font-family: Raleway;
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 21px;
`;

const Paragraph = styled.p`
  margin-top: 6px;
  font-family: Open Sans;
  font-style: normal;
  font-weight: 300;
  font-size: 14px;
  line-height: 19px;
`;

const Arrow = styled.img`
  width: 24px;
  height: 24px;
  position: absolute;
  bottom: 0;
  right: 0;
  margin-right: 10px;
  margin-bottom: 10px;
  color: #ff6b00;
`;

const ProductLister: React.FC<ProductListerProps> = ({ category }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const getCategoryData = async () => {
      try {
        console.log('The current environment is ' + process.env.NODE_ENV);

        const categoryData = await loadJsonData(`/api/product/${category}/`);
        setData(categoryData);
      } catch (e) {
        console.log(`Error when loading data for category ${category}`, e);
      }
    };
    if (!!category) {
      getCategoryData();
    }
  }, [category]);

  const products = data.map((product: Product, index) => {
    return (
      <li key={index}>
        <Article>
          <Image src={product.image} alt={product.name} />
          <Header>{product.name}</Header>
          <Paragraph>{product.description}</Paragraph>
          <Arrow src={arrowIcon} alt="" />
        </Article>
      </li>
    );
  });

  return (
    <div>
      <ul>{products}</ul>
    </div>
  );
};
export default ProductLister;
