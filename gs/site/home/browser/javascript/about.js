jQuery.noConflict();

function gs_site_home_about_init () {
      GSMoreWidget('#gs-site-home-about');
}

jQuery(window).load( function () {
    gsJsLoader.with_module('/++resource++gs-content-js-more-20130110.js', 
                           gs_site_home_about_init);
});