class Config:
    pws_base_url = None
    ps_base_url = None
    oauth_ps_url = None
    pss_url = None
    psf_url = None
    cp_url = None
    frontend_oauth_url = None
    sa_download_url = None
    view_cp_url = None

    def __init__(self, environment):
        if environment == 'staging':
            Config.pws_base_url = "https://frontend.pws-stg.px-dev.com/"
            Config.ps_base_url = "https://account-stg.px-dev.com/"
            Config.oauth_ps_url = "https://oauth-stg.ps.px-dev.com/"
            Config.psf_url = "https://frontend.psf-stg.px-dev.com/"
            Config.pss_url = "https://frontend.pss-stg.px-dev.com/"
            Config.cp_url = "http://px-twb-stg.pixellu.com/"
            Config.frontend_oauth_url = "https://frontend-oauth-stg.ps.px-dev.com/"
            Config.sa_download_url = "https://px-swb-stg-click.smartalbums.com/"
            Config.view_cp_url = "https://view-px-twb-stg.smartalbums.com/"
        elif environment == 'production':
            Config.pws_base_url = "https://www.pixellu.com/"
            Config.ps_base_url = "https://account.pixellu.com/"
            Config.oauth_ps_url = "https://auth-api.pixellu.com/"
            Config.psf_url = "https://galleries.pixellu.com/"
            Config.pss_url = "https://smartslides.com/"
            Config.cp_url = "https://cloudproofing.smartalbums.com/"
            Config.frontend_oauth_url = "https://auth.pixellu.com/"
            Config.sa_download_url = "https://click.smartalbums.com/"
            Config.view_cp_url = "https://proofalbums.com/"
        elif environment == 'prls':
            Config.pws_base_url = "https://frontend.pws-prls.px-dev.com/"
            Config.ps_base_url = "https://account-prls.ps.px-dev.com/"
            Config.oauth_ps_url = "https://oauth-stg.ps.px-dev.com/"
            Config.psf_url = "https://frontend.psf-prls.px-dev.com/"
            Config.pss_url = "https://frontend.pss-prls.px-dev.com/"
            Config.cp_url = "http://px-twb-stg.pixellu.com/"
            Config.frontend_oauth_url = "https://frontend-oauth-stg.ps.px-dev.com/"
            Config.sa_download_url = "https://px-swb-stg-click.smartalbums.com/"
            Config.view_cp_url = "https://view-px-twb-stg.smartalbums.com/"
