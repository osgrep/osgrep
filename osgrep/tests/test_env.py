from osgrep import env
import os
import unittest


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.dot = os.path.dirname(os.path.abspath(__file__))
        self.fixtures_dir = os.path.join(self.dot, 'fixtures')

    def test_config_sample(self):
        c = env.Config(os.path.join(self.dot, '..', '..',
                                    'config.sample.yaml'))
        (hosts, services) = c.build_env()

        self.assertEqual(sorted(list(hosts.keys())),
                         sorted(['example.com', 'localhost']))
        self.assertEqual(sorted(list(services.keys())),
                         sorted(['nova-compute', 'nova-api']))

        x = hosts['localhost']
        self.assertEqual(x.port, 23)
        self.assertEqual(x.identity_file, 'foobar')
        self.assertEqual(x.username, 'carrot')

        y = hosts['example.com']
        self.assertEqual(y.port, 22)
        self.assertEqual(y.identity_file, '/tmp/id_rsa')
        self.assertEqual(y.username, 'foo')

        z = services['nova-api']
        self.assertEqual(sorted([i.server.hostname for i in z]),
                         ['example.com', 'localhost'])
