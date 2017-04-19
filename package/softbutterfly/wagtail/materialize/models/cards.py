# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import BooleanBlock
from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import ChoiceBlock
from wagtail.wagtailcore.blocks import PageChooserBlock
from wagtail.wagtailcore.blocks import RawHTMLBlock
from wagtail.wagtailcore.blocks import StreamBlock
from wagtail.wagtailcore.blocks import URLBlock

from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock

from .base import MaterializeBaseStructBlock
from .base import MaterializeBaseStreamBlock

from .helpers import ColorChoices
from .helpers import TextColorChoices

from .typography import Paragraph


class CardImage(ImageChooserBlock):
    class Meta:
        label = _("Card image")


class CardTitle(MaterializeBaseStructBlock):
    contents = CharBlock(
        label=_("Card title")
    )

    materialize_class = 'card-title'
    materialize_tag = 'span'

    class Meta:
        template = 'wagtail/materialize/components/card-title.html'
        label = _("Card title")


class CardContentStreamBlock(MaterializeBaseStreamBlock):
    paragraph = Paragraph()

    class Meta:
        label = _("Card content")


class BaseCardActionBlock(MaterializeBaseStructBlock):
    contents = RawHTMLBlock(
        label=_("Text")
    )

    link = None

    materialize_class = ''
    materialize_tag = 'a'

    class Meta:
        template = 'wagtail/materialize/components/card-action.html'
        icon = "placeholder"


class CardActionToURL(BaseCardActionBlock):
    link = URLBlock(
        label=_("URL"),
        required=False,
    )

    class Meta:
        label = _("Acción a URL")

    def get_context(self, request):
        context = super(BaseCardActionBlock, self).get_context(request)
        context['action_to_url'] = True
        return context


class CardActionToBookmark(BaseCardActionBlock):
    link = CharBlock(
        label=_("Marcador"),
        required=False,
    )

    class Meta:
        label = _("Acción a marcador")

    def get_context(self, request):
        context = super(BaseCardActionBlock, self).get_context(request)
        context['action_to_bookmark'] = True
        return context


class CardActionToPage(BaseCardActionBlock):
    link = PageChooserBlock(
        label=_("Página"),
        required=False,
    )

    class Meta:
        label = _("Acción a página")

    def get_context(self, request):
        context = super(BaseCardActionBlock, self).get_context(request)
        context['action_to_page'] = True
        return context


class CardActionToDocument(BaseCardActionBlock):
    link = DocumentChooserBlock(
        label=("Documento"),
        required=False,
    )

    class Meta:
        label = _("Acción a documento")

    def get_context(self, request):
        context = super(BaseCardActionBlock, self).get_context(request)
        context['action_to_document'] = True
        return context


class CardActionToImage(BaseCardActionBlock):
    link = ImageChooserBlock(
        label=("Imagen"),
        required=False,
    )

    class Meta:
        label = _("Acción a imagen")

    def get_context(self, request):
        context = super(BaseCardActionBlock, self).get_context(request)
        context['action_to_image'] = True
        return context


class CardActionsStreamBlock(MaterializeBaseStreamBlock):
    card_action_to_url = CardActionToURL()
    card_action_to_bookmark = CardActionToBookmark()
    card_action_to_page = CardActionToPage()
    card_action_to_document = CardActionToDocument()
    card_action_to_image = CardActionToImage()

    class Meta:
        icon = 'cogs'
        label = _("Card action")


class CardActions(MaterializeBaseStructBlock):
    contents = CardActionsStreamBlock()

    color = ColorChoices(
        required=False,
    )

    materialize_class = 'card-action'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card-actions.html'
        label = _("Card Actions")


_CARD_SIZE_CHOICES = [
    ('small', _("small")),
    ('medium', _("medium")),
    ('large', _("large")),
]


class CardSizeChoice(ChoiceBlock):
    choices = _CARD_SIZE_CHOICES

    class Meta:
        label = _("Card size")
        classname = 'full'


class PanelCard(MaterializeBaseStructBlock):
    contents = CardContentStreamBlock()

    color = ColorChoices(
        required=False,
    )

    text_color = TextColorChoices(
        required=False,
    )

    materialize_class = 'card-panel'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card-panel.html'
        label = _("Panel card")


class Card(MaterializeBaseStructBlock):
    title = CardTitle()
    contents = CardContentStreamBlock()
    actions = CardActions()

    color = ColorChoices(
        required=False,
    )

    text_color = TextColorChoices(
        required=False,
    )

    materialize_class = 'card'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card.html'
        label = _("Card")


class ImageCard(MaterializeBaseStructBlock):
    image = CardImage()
    title = CardTitle()
    contents = CardContentStreamBlock()
    actions = CardActions()
    size = CardSizeChoice(
        required=False
    )

    put_image_with_title = BooleanBlock(
        label=_("Put image with title"),
        required=False,
        default=False,
    )

    add_gradient_to_title = BooleanBlock(
        label=_("Add gradient to title"),
        required=False,
        default=False,
    )

    use_horizontal_style = BooleanBlock(
        label=_("Use horizontal style"),
        default=False,
        required=False,
    )

    color = ColorChoices(
        required=False,
    )

    text_color = TextColorChoices(
        required=False,
    )

    materialize_class = 'card'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card.html'
        label = _("Image Card")


class RevealCard(MaterializeBaseStructBlock):
    image = CardImage()
    title = CardTitle()
    contents = CardContentStreamBlock()
    actions = CardActions()
    reveal_contents = CardContentStreamBlock(
        label=_("Reveal contents")
    )
    size = CardSizeChoice(
        required=False
    )

    put_image_with_title = BooleanBlock(
        label=_("Put image with title"),
        required=False,
        default=False,
    )

    add_gradient_to_title = BooleanBlock(
        label=_("Add gradient to title"),
        required=False,
        default=False,
    )

    use_sticky_action = BooleanBlock(
        label=_("Use sticky action"),
        required=False,
        default=False,
    )

    color = ColorChoices(
        required=False,
    )

    text_color = TextColorChoices(
        required=False,
    )

    materialize_class = 'card'
    materialize_tag = 'div'

    class Meta:
        template = 'wagtail/materialize/components/card.html'
        label = _("Reveal Card")


class CardsStreamBlock(StreamBlock):
    card = Card()
    panel_card = PanelCard()
    image_card = ImageCard()
    reveal_card = RevealCard()

    class Meta:
        label = _("Cards")
