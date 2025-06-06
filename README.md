 Shopno Icon Theme
======

> [!NOTE]
> This project is forked from [Nordzy Icon Theme](https://github.com/MolassessLover/Nordzy-icon) under the ownership of [@molassess](https://github.com/MolassessLover).
> The document below is a verbatim copy of what they had written under their ownership.

<p align="center">

<img src="art/preview/theme_preview.png" alt="Nordzy logo">

</p>

Shopno Icon Theme is based on Nordzy which is a free and open source  icon theme for Linux desktops using the [Nord](https://github.com/arcticicestudio/nord) color palette from [Arctic Ice Studio](https://github.com/arcticicestudio) and based on [WhiteSur Icon Theme](https://github.com/vinceliuice/WhiteSur-icon-theme) and [Numix Icon Theme](https://github.com/numixproject/numix-icon-theme)<br/>
Dark variants are more appropriate for dark desktop environments, while the normal variants are more appropriate for light desktop environments. <br/> If you are using a dark theme with a light panel (or the opposite) you can specify the panel argument which make the panel's color opposite.

## Table of contents

- [ShopnoOS Icon Theme](#nordzy-icon-theme)
  - [Table of contents](#table-of-contents)
  - [Preview](#preview)
  - [Installation](#installation)
    - [Installer](#installer)
    - [tar.gz file](#targz-file)
    - [Also available](#also-available)
  - [Uninstallation](#uninstallation)
  - [Using AppImageLauncher?](#using-appimagelauncher)
  - [Icon request](#icon-request)
  - [Contributing](#contributing)
  - [Support the author](#support-the-author)
  - [License](#license)


## Preview

![applications preview](art/preview/preview1.png)
![folders preview](art/preview/preview2.png)
![mimetype preview](art/preview/preview3.png)


## Installation
### Installer

To install the icon theme, first clone this repository
```
git clone https://github.com/JaduPC/shopno-icon
```
Then go inside it
```
cd shopno-icon/
```
and use the installer script (with or without arguments). </br>
For a local installation: 
```
./install.sh
```
For a global installation:
```
sudo ./install.sh
```


Usage:  `./install.sh`  **[OPTIONS...]**

|  OPTIONS:           | |
|:--------------------|:-------------|
|-d, --dest  DIR         | Specify theme destination directory (Default: $HOME/.icons)|
|-n, --name  NAME  | Specify theme name (Default: Nordzy)|
|-t, --theme VARIANT | Specify theme color variant(s) (default; purple; pink; red; orange; yellow; green; turquoise; cyan; all)|
|-c, --color VARIANT| Specify color variant(s) [standard;light;dark] (Default: All variants)|
|-p, --panel|Make panel's color opposite to the color variant of the theme (Default: same as color variant)|
|--total	|Install all theme, color and panel variants|
|-h, --help                 | Show  help|

### tar.gz file
Alternatively, you can use the tar.gz files located in the release section and extract them to the adequate directory.</br>
> Usually `$HOME/.local/share/icons/` for a user installation and `/usr/share/icons/` for a system wide installation.
### Also available
<p align="left">
  <a href="https://www.pling.com/p/1686927" >
    <img title="Nordzy-icon Pling Store" width="350em" src="art/banner/pling_banner.png">
  </a>
  <a href="https://aur.archlinux.org/packages/nordzy-icon-theme-git" >
    <img title="Nordzy-icon arch repo" width="350em" src="art/banner/archlinux_banner.png">
  </a>
  <a href="https://copr.fedorainfracloud.org/coprs/alvatip/Nordzy-icon/" >
    <img title="Nordzy-icon Fedora Copr" width="350em" src="art/banner/fedora_copr_banner.png">
  </a>
  <a href="https://search.nixos.org/packages?channel=23.11&from=0&size=50&sort=relevance&type=packages&query=nordzy" >
    <img title="Nordzy-icon Nix" width="350em" src="art/banner/nix_banner.png">
  </a>
</p> 


## Uninstallation
To remove the icon theme, 
If you installed it locally:
```
rm -r $HOME/.local/share/icons/Nordzy*
```
and to remove global installation:
```
sudo rm -r /usr/share/icons/Nordzy*
```

## Using AppImageLauncher?
If you are using [AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher) to manage your appimage application, running the python script AppImageIcon will update all the desktop file in $HOME/.local/share/applications/ that are created by AppImageLauncher to use Nordzy icons

```
python -m AppImageIcon
```

## Contributing

Help is always welcome.

* Create a new icon for missing applications
* Make a symlink to an existing icon
* Edit an existing icon
* Script improvement
* Spelling, grammar, etc.

## Support the author

<p align="left">
 <a href="https://www.buymeacoffee.com/alvatips" >
    <img title="Buy me a coffee banner" width="150em" src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png">
  </a>
</p>


## License

GNU General Public License v3.0.
