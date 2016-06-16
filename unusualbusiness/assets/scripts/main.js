/**
 * ub2
 * (c) (Un)usual Business <info@unusualbusiness.nl>
 */

'use strict';

import Grid from './modules/grid';
import MobileMenu from './modules/mobile-menu';
import Article from './modules/article';
import Agenda from './modules/agenda';
import Sliders from './modules/slider';
import Navbar from './modules/navbar';
import Organization from './modules/organization';
import HowTo from './modules/how-to';
import Icons from './modules/icons';
import smoothScroll from 'smooth-scroll';

(function() {
  console.log('Main: go!');

  $.expr[':'].external = function(obj){
      return !obj.href.match(/^mailto\:/)
             && (obj.hostname != location.hostname)
             && !obj.href.match(/^javascript\:/)
             && !obj.href.match(/^$/)
  };

  $(document).ready(function() {
    console.log('Main: Document ready go!');

    let grid = Grid();
    let mobileMenu = MobileMenu();
    let article = Article();
    let agenda = Agenda();
    let slider = Sliders();
    let navbar = Navbar();
    let organization = Organization();
    let howTo = HowTo();

    grid.init();
    mobileMenu.init();
    article.init();
    agenda.init();
    slider.init();
    navbar.init();
    organization.init();
    howTo.init();
  });

  $(window).ready(function() {
    console.log('Main: Window ready go!');

    let icons = Icons();
    icons.init();

    smoothScroll.init({
      selector: '[data-scroll]', // Selector for links (must be a valid CSS selector)
      selectorHeader: '[data-scroll-header]', // Selector for fixed headers (must be a valid CSS selector)
      speed: 500, // Integer. How fast to complete the scroll in milliseconds
      easing: 'easeInOutCubic', // Easing pattern to use
      offset: 28, // Integer. How far to offset the scrolling anchor location in pixels
      updateURL: true, // Boolean. If true, update the URL hash on scroll
      callback: function ( anchor, toggle ) {} // Function to run after scrolling
    });

  });
})();
