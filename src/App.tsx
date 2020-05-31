import React from 'react';
import NavBar from './components/NavBar';
import CategorySelector from './components/CategorySelector';
import { Router, RouteComponentProps } from '@reach/router';

interface ProductListerProps extends RouteComponentProps {
  productId?: string;
}

const ProductLister: React.FC<ProductListerProps> = (props) => {
  return <div>{props.productId}</div>;
};

const App: React.FC = () => {
  return (
    <div>
      <NavBar title="Mio" />
      <Router>
        <CategorySelector path="/" />
        <ProductLister path="/products/:productId" />
      </Router>
    </div>
  );
};

export default App;
