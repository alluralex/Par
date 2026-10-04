using System.Net.Http;
using System.Net.Http.Json;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ParWPF
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        HttpClient client = new();
        public MainWindow()
        {
            InitializeComponent();

            client.BaseAddress = new Uri("http://127.0.0.1:5000/api/");

            DataContext = this;
        }

        private async void GetInfoFromParser_Click(object sender, RoutedEventArgs e)
        {
            List<Message> messages = await client.GetFromJsonAsync<List<Message>>("get_products");

            messages = messages.OrderBy(m => m.Id).ToList();

            MessageName.ItemsSource = messages;
        }

        private async void CheckHealth_Click(object sender, RoutedEventArgs e)
        {
            var response = await client.GetAsync("check_health");
            if (response.IsSuccessStatusCode)
            {
                string content = await response.Content.ReadAsStringAsync();
                MessageBox.Show($"{content}");
            }
            else
            {
                MessageBox.Show($"Сервер вернул: {response.StatusCode}");
            }
        }
    }
}