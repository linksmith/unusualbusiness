/* ==|====================
   Module/Mobile Menu
   ======================= */

'use strict';

import Grid from './grid';

let MobileMenu = () => {
  let toggleHamburgerMenu = function() {
    let hamburgerMenuButtonLink = $('#hamburger-menu-button');
    let isExpanded = hamburgerMenuButtonLink.attr('aria-expanded') === 'true';
    hamburgerMenuButtonLink.attr(
        'aria-expanded',
        (!isExpanded).toString()
    );
    hamburgerMenuButtonLink.toggleClass('is-expanded');
  };

  let initAnimateMenuBar = function() {
    let menuItemHowTo = $('.main-menu-how-to');
    menuItemHowTo.addClass('is-in-position');
    // menuItemHowTo.on('click', function() {
    //   menuItemHowTo.addClass('is-fading-out');
    // });
  };
  let filterGrid = function() {
    $('.how-to-link-blue').on('click', function() {
      Grid.grid.isotope({
        filter: '.latest-article-report'
      });
    });
    $('.how-to-link-black').on('click', function() {
      Grid.grid.isotope({
        filter: '.latest-organization'
      });
    });
    $('.how-to-link-yellow').on('click', function() {
      Grid.grid.isotope({
        filter: '.latest-article-story'
      });
    });
    $('.how-to-link-green').on('click', function() {
      Grid.grid.isotope({
        filter: '.latest-article-theory'
      });
    });
  };

  let initSidrMenu = function() {
    $('#hamburger-menu-button').sidr({
      name: 'mobile-menu',
      side: 'right',
      source: '.main-nav',
      body: '.l-wrapper',
      renaming: false,
      dispace: false,
      onOpen: toggleHamburgerMenu,
      onClose: toggleHamburgerMenu
    });
  };

  let init = function() {
    initAnimateMenuBar();
    filterGrid();
    // wait for SVG's to be copied
    window.setTimeout(initSidrMenu, 1000);
  };

  return {
    init: init
  };
};

export default MobileMenu;
