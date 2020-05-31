import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

it('has a nav bar', () => {
  render(<App />);
  screen.getByRole('heading', { name: 'Mio' });
});

