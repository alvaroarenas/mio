import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

it('has a nav bar', () => {
  render(<App />);
  screen.getByRole('heading', { name: 'Mio' });
});

it('has a title', () => {
  render(<App />);
  const mainContainer = screen.getByRole('main');
  expect(mainContainer).toHaveTextContent('Select and book');
});
