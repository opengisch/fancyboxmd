# Fancybox markdown extension

This markdown extension creates [fancybox images](http://fancybox.net/).

### Markdown

```md
!![Title](image.png "Description")
```

### HTML

```html
<figure>
  <a data-caption="Description" data-fancybox="gallery" href="image.png">
    <img alt="Title" src="image.png" title="Title" width="600px" />
  </a>
  <figcaption>
    Description
  </figcaption>
</figure>
```

## Using it with mkdocs

Enable it in mkdocs.yml

```yml
markdown_extensions:
  - fancyboxmd
```

Enable fancybox in mkdocs.yml

```yml
# Css
extra_css:
  - https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css

# Extra javascript
extra_javascript:
  - https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js
  - https://cdn.jsdelivr.net/gh/fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.js
```

## Configuration

It supports one configuration option `preview_width` which defaults to `600px`.
