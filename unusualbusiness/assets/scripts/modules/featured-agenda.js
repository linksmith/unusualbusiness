/* ==|====================
   Module/Featured Agenda
   ======================= */

'use strict';

var FeaturedAgenda = () => {
  let initMouseEvents = function() {
    let agendaItemLink = $('.featured-agenda-item-link');

    agendaItemLink.on('mouseover', function() {
      let timeElement = $(this).parent().siblings().first();
      timeElement.addClass('is-hover');
    });
    agendaItemLink.on('mouseout', function() {
      let timeElement = $(this).parent().siblings().first();
      timeElement.removeClass('is-hover');
    });
  };

  let init = function () {
    console.log('Featured Agenda go!');
    initMouseEvents()
  };

  return {
    init: init
  };
};


export default FeaturedAgenda;
