import React from 'react';
import { render, screen } from '@testing-library/react';
import CategoryButton from './CategoryButton';
import 'jest-styled-components';
import carIcon from '../../assets/carIcon.svg';

it('has a text', () => {
  render(<CategoryButton label={'Cars'} />);
  screen.getByRole('button', { name: /Cars/ });
  //const imageContainer = screen.getByRole('img');
  //expect(imageContainer).not.toBeInTheDocument();
});

it('renders when given', () => {
  render(<CategoryButton label="Cars" icon={carIcon} />);
  screen.getByRole('img');
});
