from docutils import nodes
from docutils.parsers.rst import Directive


class IoTTypeDirective(Directive):
    required_arguments = 1
    optional_arguments = 0
    option_spec = {}
    has_content = False

    def run(self):
        iot_type = self.arguments[0]
        if iot_type not in {'box', 'virtual'}:
            raise ValueError('Invalid IoT type: %s' % iot_type)
        # TODO: make it a bit more sexy, like:
        # :octicon:`container` :bdg-info:`IoT box only`
        node = nodes.paragraph()
        if iot_type == 'box':
            node += nodes.Text('Only concern IoT box. Not the windows virtual IoT.')
        elif iot_type == 'virtual':
            node += nodes.Text('Only concern windows virtual IoT. Not the IoT box.')
        return [node]


def setup(app):
    app.add_directive('iot-type', IoTTypeDirective)
