from markdown.test_tools import TestCase, Kwargs
from fancyboxmd import FancyBoxExtension
import markdown

class TestHr(TestCase):
    default_kwargs = Kwargs(
        extensions=[FancyBoxExtension()],
    )

    def test_with_width(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                """
                !![Registration](../../assets/images/qfieldcloud_registration.png, 69px)
                """
            ),
            # The expected HTML output
            self.dedent(
                """
                <p>
                <figure><a data-caption="Registration" data-fancybox="gallery" href="../../assets/images/qfieldcloud_registration.png"><img alt="Registration" src="../../assets/images/qfieldcloud_registration.png" title="Registration" width="69px"></a><figcaption>Registration</figcaption>
                </figure>
                </p>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            output_format='html'
        )

    def test_without_width(self):
        self.assertMarkdownRenders(
            # The Markdown source text used as input
            self.dedent(
                """
                !![Registration](../../assets/images/qfieldcloud_registration.png)
                """
            ),
            # The expected HTML output
            self.dedent(
                """
                <p>
                <figure><a data-caption="Registration" data-fancybox="gallery" href="../../assets/images/qfieldcloud_registration.png"><img alt="Registration" src="../../assets/images/qfieldcloud_registration.png" title="Registration" width="600px"></a><figcaption>Registration</figcaption>
                </figure>
                </p>
                """
            ),
            # Other keyword arguments to pass to `markdown.markdown`
            output_format='html'
        )
