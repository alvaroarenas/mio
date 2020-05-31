import React from 'react';
import { render, screen } from '@testing-library/react'
import CategorySelector from './CategorySelector'

it('has a title', () => {
  render(<CategorySelector />);
  const mainContainer = screen.getByRole('main');
  expect(mainContainer).toHaveTextContent('Select and book');
});

it('has buttons', () => {
  render(<CategorySelector />);
  const buttons = screen.getAllByRole('button').map((el) => el.textContent);
  expect(buttons.length).toBe(4);
});
