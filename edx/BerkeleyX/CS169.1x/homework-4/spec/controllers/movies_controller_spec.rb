require 'spec_helper'

describe MoviesController do
  fixtures :movies

  before :each do
    @similar = Movie.find_all_by_director Movie.find(1).director
  end

  describe 'similar movies' do
    it 'should call the model method that search for similar movies' do
      Movie.should_receive(:similar_to).and_return(@similar)
      get :similar, {:movie => 1}
    end
    it 'should select the Find Similar template for rendering' do
      Movie.stub(:similar_to).and_return(@similar)
      post :similar, {:movie => 1}
      response.should render_template('similar')
    end
    it 'should make similar movies available to that template' do
      Movie.stub(:similar_to).and_return(@similar)
      post :similar, {:movie => 1}
      assigns(:movies).should == Movie.find_all_by_director('George Lucas')
    end
  end

end