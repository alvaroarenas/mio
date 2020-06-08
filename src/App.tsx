import React from 'react';
import NavBar from './components/NavBar';
import CategorySelector from './components/CategorySelector';
import ProductLister from './components/ProductLister';
import { Router } from '@reach/router';

const App: React.FC = () => {
  return (
    <div>
      <NavBar title="Mio" />
      <Router>
        <CategorySelector path="/" />
        <ProductLister path="/products/:category" />
      </Router>
    </div>
  );
};

export default App;
